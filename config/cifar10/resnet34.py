trainer = dict(type='AntiKDTrainer',
               teacher=dict(network=dict(arch='cifar',
                                         type='resnet18',
                                         num_classes=10),
                            optimizer=dict(type='SGD',
                                           lr=0.05,
                                           momentum=0.9,
                                           weight_decay=5e-4),
                            scheduler=dict(type='CosineAnnealingLR',
                                           T_max=100),
                            lambda_t=0.1,
                            lambda_mask=1e-4,
                            trainable_when_training_trigger=False),
               students=dict(
                   resnet18=dict(network=dict(arch='cifar',
                                              type='resnet18',
                                              num_classes=10),
                                 optimizer=dict(type='SGD',
                                                lr=0.05,
                                                momentum=0.9,
                                                weight_decay=5e-4),
                                 scheduler=dict(type='CosineAnnealingLR',
                                                T_max=100),
                                 lambda_t=1e-2,
                                 lambda_mask=1e-4,
                                 trainable_when_training_trigger=False),
                   vgg16=dict(network=dict(arch='cifar',
                                           type='vgg16',
                                           num_classes=10),
                              optimizer=dict(type='SGD',
                                             lr=0.05,
                                             momentum=0.9,
                                             weight_decay=5e-4),
                              scheduler=dict(type='CosineAnnealingLR',
                                             T_max=100),
                              lambda_t=1e-2,
                              lambda_mask=1e-4,
                              trainable_when_training_trigger=False),
                   mobilenet_v2=dict(network=dict(arch='cifar',
                                                  type='mobilenet_v2',
                                                  num_classes=10),
                                     optimizer=dict(type='SGD',
                                                    lr=0.05,
                                                    momentum=0.9,
                                                    weight_decay=5e-4),
                                     scheduler=dict(type='CosineAnnealingLR',
                                                    T_max=100),
                                     lambda_t=1e-2,
                                     lambda_mask=1e-4,
                                     trainable_when_training_trigger=False),
               ),
               trigger=dict(network=dict(arch='trigger',
                                         type='trigger',
                                         size=32),
                            optimizer=dict(type='Adam', lr=1e-2),
                            mask_clip_range=(0., 1.),
                            trigger_clip_range=(-1., 1.),
                            mask_penalty_norm=2),
               clean_train_dataloader=dict(dataset=dict(
                   type='CIFAR10',
                   root='data/cifar/cifar10',
                   train=True,
                   download=True,
                   transform=[
                       dict(type='RandomCrop', size=32, padding=4),
                       dict(type='RandomHorizontalFlip'),
                       dict(type='ToTensor'),
                       dict(type='Normalize',
                            mean=(0.4914, 0.4822, 0.4465),
                            std=(0.2023, 0.1994, 0.2010))
                   ]),
                                           batch_size=32,
                                           num_workers=4,
                                           pin_memory=True),
               clean_test_dataloader=dict(dataset=dict(
                   type='CIFAR10',
                   root='data/cifar/cifar10',
                   train=False,
                   download=True,
                   transform=[
                       dict(type='ToTensor'),
                       dict(type='Normalize',
                            mean=(0.4914, 0.4822, 0.4465),
                            std=(0.2023, 0.1994, 0.2010))
                   ]),
                                          batch_size=32,
                                          num_workers=4,
                                          pin_memory=True),
               poison_train_dataloader=dict(dataset=dict(
                   type='TargetRatioCIFAR10',
                   target=1,
                   ratio=0.1,
                   root='data/cifar/cifar10',
                   train=True,
                   download=True,
                   transform=[
                       dict(type='RandomCrop', size=32, padding=4),
                       dict(type='RandomHorizontalFlip'),
                       dict(type='ToTensor'),
                       dict(type='Normalize',
                            mean=(0.4914, 0.4822, 0.4465),
                            std=(0.2023, 0.1994, 0.2010))
                   ]),
                                            batch_size=32,
                                            num_workers=4,
                                            pin_memory=True),
               poison_test_dataloader=dict(dataset=dict(
                   type='TargetRatioCIFAR10',
                   target=1,
                   ratio=1,
                   root='data/cifar/cifar10',
                   train=False,
                   download=True,
                   transform=[
                       dict(type='ToTensor'),
                       dict(type='Normalize',
                            mean=(0.4914, 0.4822, 0.4465),
                            std=(0.2023, 0.1994, 0.2010))
                   ]),
                                           batch_size=32,
                                           num_workers=4,
                                           pin_memory=True),
               epochs=100,
               save_interval=5,
               temperature=1.0,
               alpha=1.0,
               device='cuda')
